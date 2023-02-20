from typing import List

class Frame:
    def __init__(self, beginnings, ends):
        self.beginnings = beginnings
        self.ends = ends

    def __repr__(self):
        return f'Frame: {self.beginnings} beginnings and {self.ends} ends'

    def __str__(self):
        return f'Frame: {self.beginnings} beginnings and {self.ends} ends'
    
class Block: 
    # Everything is a Block.
    # Blocks make the 4D projection.
    # Each Block is made of Frames (3D).
    def __init__(self, frames):
        self._frames = frames

    def add_frame(self, frame: Frame) -> None:
        self._frames += [frame]

    def get_frames(self) -> List[Frame]:
        return self._frames

    def __str__(self):
        s = ''.join(str(self._frames))
        return str(f'Block: {s}')
    
if __name__ == '__main__':
    # 4D computation indexing should start at
    # 1 since 0 beginnings is Nothing (None in Python).
    f1 = Frame(1,0)
    f2 = Frame(1,0)
    b = Block([f1,f2])
    print(b)