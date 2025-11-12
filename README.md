# PyCPBoost

นี่คือโปรเจกต์ทดลองสำหรับการสร้าง Python C++ Extension โดยใช้ C API (Python.h) โดยตรง

เป้าหมายของโปรเจกต์นี้คือเพื่อเรียนรู้:
* วิธีการเชื่อม (Bind) โค้ด C++ ให้ Python เรียกใช้ได้
* ศึกษาเรื่อง "Overhead" (ต้นทุนแฝง) ของการเรียกฟังก์ชัน
* พิสูจน์ว่า C++ จะเร็วกว่า Python มหาศาลเมื่องานประมวลผล "หนัก" (Heavy Computation)

## คุณสมบัติ (Features)

โมดูลนี้มี 3 ฟังก์ชัน:
* `add(a, b)`: บวกเลข (long long)
* `multiply(a, b)`: คูณเลข (double)
* `heavy_loop(n)`: วนลูปบวกเลขตั้งแต่ 0 ถึง n (เพื่อทดสอบงานหนัก)

## วิธีการ Build (คอมไพล์)

โปรเจกต์นี้ใช้ `setuptools` ในการคอมไพล์

1.  ตรวจสอบว่าคุณมี C++ Build Tools (เช่น Visual Studio Build Tools บน Windows)
2.  รันคำสั่ง:
    ```bash
    python setup.py build_ext --inplace
    ```
3.  จะได้ไฟล์ `first_extension.pyd` (หรือ `.so` บน Linux) ในโฟลเดอร์เดียวกัน

## วิธีการใช้งาน (Python)

```python
import first_extension

print(first_extension.add(10, 20))

print(first_extension.multiply(5.5, 2.0))

result = first_extension.heavy_loop(10000000) 
print(result)
```

## ผลการทดสอบประสิทธิภาพ (Benchmark)

นี่คือผลลัพธ์ที่พิสูจน์แนวคิดเรื่อง Overhead:

**การทดสอบงานเบา (Add/Multiply): Python ชนะ**
* Pure Python (Add): 0.323 วินาที
* C++ Extension (Add): 0.479 วินาที (ช้ากว่าเพราะ Overhead)
* Pure Python (Multiply): 0.332 วินาที
* C++ Extension (Multiply): 0.568 วินาที (ช้ากว่าเพราะ Overhead)

**การทดสอบงานหนัก (Heavy Loop): C++ ชนะขาดลอย**
* Pure Python (Loop 10 ล้านครั้ง): 0.240 วินาที
* C++ Extension (Loop 10 ล้านครั้ง): **0.002 วินาที** (เร็วกว่าประมาณ 92-93 เท่า)

**สรุป:** C++ Extension ไม่ได้เร็วขึ้นสำหรับงานเล็กๆ แต่จะเร็วกว่ามหาศาลเมื่องานประมวลผลเกิดขึ้น "ภายใน" C++ ทั้งหมด