<h4> Run Program </h4>

`- pip install -r requirements.txt`

`- python3 main.py`

<h4> For Test: </h4>

```
 python3 -m unittest -v
```

<h4> Input: </h4>

- Link_Station:
    ```
    [[0, 0, 10],
    [20, 20, 5],
    [10, 0, 12]]
    ```
- Point:
    ```
    (0,0), (100, 100), (15,10) and (18, 18).
    ```

<h4>Output</h4>

```
Best link station for point 0,0 is 0,0 with power 100.0
No link station within reach for point 100,100
Best link station for point 15,10 is 10,0 with power 0.6718427000252355
Best link station for point 18,18 is 20,20 with power 4.715728752538098
```