(* ::Package:: *)

BeginPackage["SDSS`"]
SQLQuery::usage= "SQLQuery[q] issue an SQL query to SDSS database"
GetSpec::usage= "GetSpec[s] Get Spectrum s"

Begin["`Private`"]

SQLQuery[ q_ ] := Module[{},
						cmd="!python /home/pi/Mathematica/SDSS/sdss_query.py \""<>q<>"\"";
						Import[cmd,"String"];
						Get["/ram/Results"];
						Return[Import["/ram/Vars"]]
                       ];
GetSpec[ s_ ] := Module[{},
						cmd ="!python /home/pi/Mathematica/SDSS/sdss_getSpec.py "<>IntegerString[s];
						Import[cmd,"String"];
                         Get["/ram/Results"];
                         Return[Import["/ram/Vars"]];
                        ];

End[]
EndPackage[]
