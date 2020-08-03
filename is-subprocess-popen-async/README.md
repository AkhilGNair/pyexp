### Results

`Popen` launches all the processes concurrently and `communicate` will for them to finish.

```
Begin program
--- start: using run ---
`using_run` 10 times took 2.057 seconds to run.
--- end: using run ---
--- start: using Popen ---
`using_Popen` 10 times took 0.213 seconds to run.
--- end: using Popen ---
End program
```

