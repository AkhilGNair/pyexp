# Experiments

Galaxy brain IDE

```
poll() { 
    while true; do p=$(stat -c=%y $1); if [ "$p" != "$q" ]; then q=$p; python run.py; fi;  sleep 0.5; done;
}
```
