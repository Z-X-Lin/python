a=input()
if "."in a or "e" in a or "E" in a:
    a=float(a)
else:
    a=int(a)
print("%.6f"%a)
print(f"{a:>012.3f}")
print(f"{round(a):>010d},{a:<010.3f}")