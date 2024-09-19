# Project PAPAtools

My research on a number of Parallel Application Performance Analysis Tools.

Initiator: POP-CoE course on Profiling and Optimisation Tools. Focus on Paraver and Scalasca.

### Links
- A [Recent article](litterature/1-s2.0-S0167739X24004187-main.pdf) about these tools.
- [VIRTUAL INSTITUTE — HIGH PRODUCTIVITY SUPERCOMPUTING](https://www.vi-hps.org)



## Paraver

[Paraver](https://tools.bsc.es/paraver/) uses [Extrae](https://tools.bsc.es/extrae) for measuring performancd metrics and [Dimemas](https://tools.bsc.es/dimemas) to simulate outcomes on different networks.

### Links
[Introduction to Paraver (Youtube)](https://www.youtube.com/watch?v=R8_EhVpOzb0) 

## Scalasca
[Scalasca](https://www.scalasca.org) which uses [Score-P](https://www.vi-hps.org/projects/score-p) for measuring performance metrics and [Cube](https://www.scalasca.org/scalasca/software/cube-4.x/download.html) for exploring the performance report.
Score-P uses LD_PRELOAD to instrument application codes (a stackoverflow issue on [LD_PRELOAD](https://stackoverflow.com/questions/426230/what-is-the-ld-preload-trick)).

### Links

## Using Extrae on Vaughan

    > ml Extrae/4.0.4-gompi-2022a
    > . $EBROOTEXTRAE/etc/extrae.sh
