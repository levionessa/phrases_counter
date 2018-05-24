## Phrases Exercise

### Testing

Run `python test.py`.

If it prints "Tests pass" it's fine.

If you get an assertion error, the output looks wrong.


### Notes & Caveats

* The test is intentionally not the best to cope with a busy schedule.
  Were I to continue on this as a project,
  the first thing I'd do is construct a real test;
  likely one that generates understood text where values are known instead of me being pretty confident and writing a test to that confidence.
* Performance testing would be at another level.
  (Might involve real logs from an environment if we're talking gigs).
  * If performance proved to be an issue,
    that's when I'd break out trying to parallelize this in some way.
    For a two hour project with one suggestion using list comprehensions and python functions like `translate` felt efficient enough.
    (Felt meaning I as a human didn't feel like I was waiting)
    Real things might need real measurements.
