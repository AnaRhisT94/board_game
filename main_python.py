import time
from candidate_solution import Board

MIN_TIME_FOR_NOTICE = 0.0

def time_measure(func):
    def func_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        run_time = time.time() - start_time
        if run_time > MIN_TIME_FOR_NOTICE:
            print("Run Time of %s: %.2f msec" % (func.__name__, run_time*1000))
        return result
    return func_wrapper


@time_measure
def init_board(width, height, red_locs, green_locs):
    return Board(width, height, red_locs, green_locs)


@time_measure
def find_best_coordinates(board, max_red):
    return board.find_best_coordinates(max_red)


def test_for_case(board, max_red, possible_locs=None, possible_xs=None, possible_ys=None):
    p = find_best_coordinates(board, max_red)
    
    print(p)
    if (possible_locs is None or tuple(p) in possible_locs) and \
        (possible_xs is None or p[0] in possible_xs) and \
        (possible_ys is None or p[1] in possible_ys):
        pass
        # Success
    #else:
       # print("*** Failed for max_red=%d. Given Answer: (%d, %d)" % (max_red, p[0], p[1]))

def test_board():
    print("Testing 3x1 board...")
    red_locs    = [(0,0), (1,0), (2,0)]
    green_locs  = [(1,0), (2,0)]
    board       = Board(3, 1, red_locs, green_locs)
    test_for_case(board, 2, [(1,0)])

    print("Testing 10,000 x 3 board...")
    red_locs = [(9000, 0), (1200, 2), (5000, 1)]
    board = init_board(10000, 3, red_locs, green_locs)
    find_best_coordinates(board, 2)


if __name__ == "__main__":
    test_board()