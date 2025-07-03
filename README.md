# 2018S1SEQUOIACommissioning 

The usual Commissioning projects

Oddly enough, NGC628 also has a few obsnums stored here. Possibly a mistake, since it
is part of 2018-S1-MU-8

For IRC+10216 see the ARO 3mm spectral line survey in https://arxiv.org/abs/2507.00434

A single obsnum detects both 12CO and SiC2 @ 115.3824 GHz. and maybe something at 115.5524 (-750 km/s on CO)

A full spectrum shows three birdies at channels
   1184-1185
   1262
   1368-1369
which normally don't show in the default dv=100 dw=250 of bench2 (obsnum 79448).
Try dv=200 dw=800 to view them,  but you will also see the Tsys drop at the low V (high channel) end.

lmtinfo.py grep IRC+10216  | grep -v Cal|grep -v Focus | grep -v Asti | grep SEQ | grep -v 1MM | grep Map

this has mostly 115GHz, but also some 110 (13CO) GHz.    (5/61 are in 13CO, rest 12CO)

