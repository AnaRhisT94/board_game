Installation: 
---------
Use `main_python.py` to run the code of `solution_candidate.py`

Scenario: 
---------

- On a checkerboard of size MxN, there are red and green pieces.

- Each square on the board may contain any number of pieces, of any color. **(We can have 5 pieces - 3 green and 2 red in the same square, or  for e.g. green green, or red red, or whatever number)**

- I'm looking for an axis-aligned rectangle on the board with as many green pieces as possible.

- However, the rectangle may not contain more than a given number of red pieces.

- One corner of the rectangle must be (0,0).

Example:
--------

Board size is 6x4, red pieces are marked "x", green pieces are marked "o".

<pre>
      +-+-+-+-+-+-+
    3 | | | |o|x|o|
      +-+-+-+-+-+-+
    2 |o| |x| | |o|
      +-+-+-+-+-+-+
    1 |o| |o| |o|x|
      +-+-+-+-+-+-+
    0 | |o| |x| |x|
      +-+-+-+-+-+-+
       0 1 2 3 4 5
</pre>

- If we allow 2 red pieces, then (4,2) is an optimal solution, because the area between (0,0) and (4,2) contains 5 green pieces and 2 red pieces.
 No point with up to 2 red pieces contains more than 5 green pieces. (3,3) is also an optimal solution.

- If we allow 3 red pieces, then (4,3) is the only optimal solution, with 6 green pieces.

**I'm given:**

- the board size, 
- the coordinates of all green and red pieces, 
- the number of allowed red pieces ("maxRed")

**Goal:**
For any given "maxRed", the class should be able to calculate coordinates (x,y) such that the axis-aligned rectangle between (0,0) and (x,y) contains at most "maxRed" red pieces, and the number of green pieces is maximal.
