# height-of-trees
comparing AVL Tree's height, RB Tree's height with const logN

# Yêu cầu bài toán
- Tạo 10 bộ dữ liệu ngẫu nhiên, mỗi bộ có khoảng 10^6 giá trị
- Cài đặt cây AVL và cây Đỏ-Đen
- Chạy thử việc tạo cây bằng cách thêm lần lượt các số bộ dữ liệu đã tạo
- Ghi nhận chiều cao cây, vẽ biểu đồ so sánh các chiều cao cây và giá trị logN, 1.45logN 
- Viết báo cáo thực nghiệm

# Giải quyết
- Do không có yêu cầu về thời gian nên em sử dụng python để giải quyết

## Chương trình chính
- File main
```python
import os
import random
import math
import matplotlib.pyplot as plt
import csv

from generate import gen
from AVLtree import Node, AVL_Tree
from RBtree import Node, RB_Tree
from execute import run
from visualize import print_out

A = 1e6 - 1e3                           ## Hằng số chặn dưới tạo dữ liệu
B = 1e6                                 ## Hằng số chặn trên tạo dữ liệu

def main():
    gen(A, B)                           ## Để tạo các bộ dữ liệu
    res = run()                         ## Tính toán chiều cao, trả về địa chỉ file kết quả (.csv)
    print_out(res)                      ## Vẽ biểu đồ đường dựa trên file kết quả

if __name__ == "__main__":
    main()
```
## Dữ liệu
- Tạo ngẫu nhiên ~ 1 triệu số
- Không mất tính tổng quát, em chọn khoảng random là từ 0 -> 1 tỉ, số nguyên
- Code chi tiết tại file [generate](https://github.com/whynotkimhari/height-of-trees/blob/main/generate.py)

## Cây cối: AVL và RB
- Em chỉ thiết lập phương thức thêm node vào các cây, ngoài ra không có những phương thức khác như xoá node,...
- Còn có những phép xoay cây đi kèm: xoay trái, xoay phải
- Code được tham khảo tại Geeks
- Chi tiết file: [AVL](https://github.com/whynotkimhari/height-of-trees/blob/main/AVLtree.py), [RB](https://github.com/whynotkimhari/height-of-trees/blob/main/RBtree.py)

## Tính toán
- Mỗi lần xử lí một bộ dữ liệu, tính toán chiều cao của cây AVL/RB khi thêm các số vào cây
- Kết quả xuất ra là file .csv chứa thông tin chiều cao và hằng số logN ở mỗi trường hợp
- Chi tiết tại file [execute](https://github.com/whynotkimhari/height-of-trees/blob/main/execute.py)

## Biểu đồ
- Sử dụng thư viện matplotlib vẽ biểu đồ đường, chi tiết tại file [visualize](https://github.com/whynotkimhari/height-of-trees/blob/main/visualize.py), như sau:
![chart](https://github.com/whynotkimhari/height-of-trees/blob/main/chart.png)

# Đánh giá
- Sau thực nghiệm, em đã thấy rõ mối quan hệ giữa chiều cao các cây đã được học trong tiết:
- $hAVL < 1.45 \times hCBT$
- $logN \leqslant hRB \leqslant 2 \times logN$
- Trong báo cáo này, $hAVL \leqslant hRB, \forall dataset$
- Hiểu được sự tiết kiệm chi phí khi dùng cây AVL/RB để lưu trữ
