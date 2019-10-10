import numpy as np
arr0 = np.matrix([-1,1,1,1,-1,\
1,-1,-1,-1,1,\
1,-1,-1,-1,1,\
1,-1,-1,-1,1,\
1,-1,-1,-1,1,\
-1,1,1,1,-1])
arr1 = np.matrix([-1,1,1,-1,-1,\
-1,-1,1,-1,-1,\
-1,-1,1,-1,-1,\
-1,-1,1,-1,-1,\
-1,-1,1,-1,-1,\
-1,-1,1,-1,-1])
arr2 = np.matrix([1,1,1,-1,-1,\
-1,-1,-1,1,-1,\
-1,-1,-1,1,-1,\
-1,1,1,-1,-1,\
-1,1,-1,-1,-1,\
-1,1,1,1,1])
arrw = arr0.getT().dot(arr0)+arr1.getT().dot(arr1)+arr2.getT().dot(arr2)
print('请输入6X5图像矩阵，以空格分隔，1代表黑色，-1代表白色，以回车结束：')
print('注意：如[-1,1,1,1,-1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,1,-1,-1,-1,1,-1,1,1,1,-1]是数字0')
test1 = [int(n) for n in input().split()]
test = np.matrix(test1)
out = arrw.dot(test.getT())
for i in range(out.size):
    if(out[i]>0):
        out[i] = 1
    else:
        out[i] = -1
out = out.getT()
if (out==arr0).all():
    print('识别结果为0')
elif (out==arr1).all():
    print('识别结果为1')
else:
    print('识别结果为2')