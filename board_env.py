# board_env.py
import numpy as np
from PIL import Image

class BoardEnv:
    def __init__(self, size=10, cell_size=20):
        """
        size: number of cells in one dimension (size x size grid)
        cell_size: pixel size of each cell when rendered
        """
        self.size = size
        self.cell_size = cell_size
        self.board = np.zeros((size, size), dtype=np.uint8)

    def reset(self):
        """Reset board to all zeros."""
        self.board.fill(0)
        return self.board

    def set_cell(self, r, c, value):
        """Set a specific cell to a value (0,1,2,...)."""
        if 0 <= r < self.size and 0 <= c < self.size:
            self.board[r, c] = value

    def get_state(self):
        """Return the raw board (NumPy array)."""
        return self.board.copy()

    def render_to_array(self):
        """
        Render board to an RGB NumPy array.
        Colors are mapped based on cell values.
        """
        h, w = self.size, self.size
        cell = self.cell_size

        # Default color map (can be extended)
        colors = {
            0: (0, 0, 0),       # empty - black
            1: (0, 255, 0),     # green
            2: (255, 0, 0),     # red
            3: (0, 0, 255),     # blue
        }

        img = np.zeros((h * cell, w * cell, 3), dtype=np.uint8)

        for r in range(h):
            for c in range(w):
                color = colors.get(self.board[r, c], (255, 255, 255))
                img[r*cell:(r+1)*cell, c*cell:(c+1)*cell] = color

        return img

    def render_pil(self):
        """Return a PIL Image of the board."""
        arr = self.render_to_array()
        return Image.fromarray(arr)


# For quick testing:
if __name__ == "__main__":
    env = BoardEnv(size=10, cell_size=30)
    env.reset()

    # Draw a green square (value=1)
    env.set_cell(3, 3, 1)
    env.set_cell(3, 4, 1)
    env.set_cell(4, 3, 1)
    env.set_cell(4, 4, 1)

    img = env.render_pil()
    img.show()
