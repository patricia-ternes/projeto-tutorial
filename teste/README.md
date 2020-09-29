# Trajectory reconstruction process
A interval of the Grand Central Terminal (NewYork City) data was selected and processed.

## Video interval
From frame 20000 to frame 23000

## Perspective correction
$$ (x, y) = (x', y')[1 + \delta]$$

* $$\delta=y'/h'$$
* $$x$$': pedestrian horizontal position before transformation
* $$y$$': pedestrian vertical position before transformation
* $x$: pedestrian horizontal position after transformation
* $y$: pedestrian vertical position after transformation