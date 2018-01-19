Copyright (c) John Henri, All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice


**simplePlot**

The idea behind simplePlot is to create simple tool that will graph a set of numbers
that came out of some benchmark data of something that runs periodically.  If it
succeeded, the benchmark would write the time (in seconds) in a unique text file.
simplePlot reads in those files and creates a line chart in time ascending order.

**Example Output**

Here is a sample output:

![alt text](https://github.com/jakojon/public_tools/blob/master/simplePlot/example.png "Example output")

You can get this by:

  simplePlot.py --directory ~/DATA/ "d.*.txt" --label "Processing time in seconds"

If you have the following files in the ~/DATA/ directory

```
> cat d.1.txt
  122
> cat d.2.txt
  124
> cat d.3.txt
  123
> cat d.4.txt
  140
> cat d.5.txt
  122
> cat d.6.txt
  130
```

NOTE: That the script will sort the files by create time