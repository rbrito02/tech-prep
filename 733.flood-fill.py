# @leet start
from collections import deque
from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        if not image or image[sr][sc] == color:
            return image

        original_color = image[sr][sc]
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]

        q = deque()
        q.append((sr, sc))

        while q:
            x, y = q.popleft()

            # Fill the color
            image[x][y] = color

            # Enqueue neighbors with the same original color
            for i in range(4):
                newX = x + dx[i]
                newY = y + dy[i]
                if (
                    self.inRange(image, newX, newY)
                    and image[newX][newY] == original_color
                ):
                    q.append((newX, newY))

        return image

    def inRange(self, image: List[List[int]], x: int, y: int) -> bool:
        return 0 <= x < len(image) and 0 <= y < len(image[0])


# @leet end

