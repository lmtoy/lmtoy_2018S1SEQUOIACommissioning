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

##  combo

76406,77385,77387,77389,77493,77495,77497,77497,77499,77500,77501,77502,77503,77504,77715,77717,77719,77722,77723,77725,77727,77729,77731,77733,77735,77736,77737,77818,77820,77990,77992,77994,77996,77998,78063,78063,78065,79440,79442,79444,79446,79448,82666,82668,82695,95121,95123,95125,100034,100035,100037,111259


Here is a run with both strong lines in one cube:

```
SLpipeline.sh obsnum=79448 restart=1 map_coord_use=1 vlsr=-170 dv=250 dw=200 birdies=1368,1369
```

has some birdies.  In addition to the CO and SiC2 lines, there are at least two other
very weak lines visible in the combination:

```
vlsr   TdV   line   restfreq
-20   215971 CO     115.2712
-310   14807 SiC2   115.382367
-750     657 C4H    115.5451
-890    1012 C3S    115.6080 blend
             H2CCCC 

+120    1960 C4H  115.2168
```
The TdV integral is mK.km/s and is taken from the ARO survey.

## ARO survey

Channels are 197 kHz. (LMT has 390 kHz, twice as wide).  40 mins on-source time per bands.
For ARO and Tsys=100 a 40 min intregration gives 4.6 mK RMS.


12CO:  
13CO:  5 good, of which 1 is full 'C' map, 4 are smaller 'D' maps





