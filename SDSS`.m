(* ::Package:: *)

BeginPackage["SDSS`"]
SQLQuery::usage= "SQLQuery[q] issue an SQL query to SDSS database"
GetObjSpec::usage= "GetObjSpec[obj] Get Spectrum of Object"

Begin["`Private`"]

SQLQuery[ q_ ] := Module[{},
						cmd="!python /home/pi/Mathematica/SDSS/sdss_query.py \""<>q<>"\"";
						Import[cmd,"String"];
						Get["/ram/Results"];
						Return[Import["/ram/Vars"]]
                       ];
GetObjSpec[ obj_ ] := Module[{},
						SQLQuery["select top 1 plate,mjd,fiberID from SpecObj where bestObjID = "<>IntegerString[obj]];
						plate = Import["/ram/xfer-plate"];
						mjd2 = Import["/ram/xfer-mjd"];
						fiberID = Import["/ram/xfer-fiberID"];
						cmd ="!python /home/pi/Mathematica/SDSS/sdss-DR12_getSpec.py "<>IntegerString[obj]<>" ";
                        cmd = cmd<>plate<>" "<>mjd2<>" "<>fiberID<>" V5_7_0";
						(*cmd2 = "!python /home/pi/Mathematica/SDSS/sdss-DR12_getSpec.py 1237652901285003577 650 52143 481 V5_7_0";*)
						Import[cmd,"String"];					    
						 (*Return[cmd];*)\[AliasDelimiter]
						Get["ram/Results"];
                         Return[Import["/ram/Vars"]];
                        ];

End[]
EndPackage[] 



