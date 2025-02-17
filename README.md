
CNC + Fiber Laser PCB 

![Screenshot](pics/engraved.jpeg)

You can make a PCB with a CNC.

You can make a PCB with a Fiber Laser.

By matching the appropriate technology to the task you can make a high quality small batches of PCBs quickly.

CNCs are excellent for making deep cuts and drilling holes.

Fiber Lasers excel at making fine pitch traces.

CNCs are inexpensive. 

Fiber lasers are relatively expensive.

This method avoids:
* charring
* excess fumes
* uneven depth cuts
* overdriving fiber laser

This method allows for:
* faster traces due copper / resin size
* vias
* double sided (for schizzle)
* more laser time for other jobs

```
         +-----------------+
         |   PCB Material  |
         +-----------------+
                  |
         +--------+--------+
         |                 |
         V                 V
+----------------+   +---------------+
|  CNC Machine   |   | Fiber Laser   |
| (Edge & Drilling)  | (Traces)     |
+----------------+   +---------------+
         |                 |
         +--------+--------+
                  |
         +-----------------+
         |   Completed PCB |
         +-----------------+
```

Laser Settings
===
|      Type       | Power (%) | Speed (mm/s) | Pass (#x) | Time | Desc                                                                 |
|:---------------:|:---------:|:------------:|:---------:|:----:|:--------------------------------------------------------------------:|
| Trace Cut       | 80        | 3000         | 25        | 30s  | just right                                                         |
| Trace Engrave   | 100       | 6000         | 10        | 12m  | pretty clean                                                       |
| Stencil Cut     | 80        | 300          | 120       | 2m   | Yep! Looks cooked, but was almost 100% through with no damage to brass |
| pcb cut         | 100       | 100          | 160       | 5m   | some smoke (use CNC if possible)                                   |



Materials
===

|                 Item                                    | Price | Source |
|:-------------------------------------------------------:|:-----:|:------:|
| [xTool F1 Ultra 20W Fiber](https://amzn.to/41h2cZH)      | 4200  | Amazon |
| [Andonstar AD246S-M Digital Microscope](https://amzn.to/41iweML) | 140  | Amazon |
| [MHP50](https://amzn.to/4gItVXV)                         | 140   | Amazon |
| [10 Pcs Single Sided Copper Clad PCB](https://amzn.to/4jXkF4V) | 7     | Amazon |
| [Low Temp Solder Paste](https://amzn.to/42WLXSY)         | 21    | Amazon |
| [Brass 0.1mm Stencil Material](https://amzn.to/42XMIes)  | 10    | Amazon |
| [Gloves Anti-Static](https://amzn.to/3X36cKU)            | 17     | Amazon |
| [PCB Stencil Jig Knobs](https://amzn.to/42TYsPh)         | 10    | Amazon |
| [PCB Stencil Jig Feet](https://amzn.to/4i0Jrzc)           | 10    | Amazon |
| [PCB Stencil Jig Knurled Nuts](https://amzn.to/3X5jerg)    | 10    | Amazon |

How about a Solder Mask and Silkscreen
===
Applying a coating to protect the PCB is a good idea. Not only does it look amzing, but it will protect the PCB. 

A silkscreen helps with correct component placemen, location and identification information. 

Both of these layers add substantial time and some different materials to apply correctly. I'll hold off on 
addressing these issues for another video / github.

Acknowledgements
===
Special thanks to both of these excellent folks for sharing their open hardware designs in this area.

* [Stephen Hawes Fiber Laser PCB Fab](https://github.com/sphawes/fiber-laser-pcb-fab)
* [makermoekoe StencilJig3D](https://github.com/makermoekoe/StencilJig3D/tree/main)
