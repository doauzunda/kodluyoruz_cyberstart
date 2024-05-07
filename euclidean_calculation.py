### GÖREVİNİZ ###
# python' da fonksiyonlar ve döngüler kavramlarını kullanarak,
# aşağıdaki işlemleri gerçekleştiren bir program yazmanız gerekmektedir.

### NOKTALARIN TANIMLANMASI ###
# "points" adında bir liste oluşturun
# bu liste, 2D uzaydaki noktaları temsil eden demetler (tuple) içermelidir
# örneğin (x, y) noktası bir demet (x, y) oalrak temsil edilecektir.

### ÖKLİD MESAFESİ İÇİN BİR FONKSİYON YAZMA ###
# "euclideanDistance" adında bir fonksiyon tanımlayın.
# bu fonksiyon, iki demet (her biri bir noktayı temsil eder) almalı
# ve bu iki nokta arasındaki öklid mesafesini döndürmelidir

### MESAFELERİN HESAPLANMASI ###
# bir döngü kullanarak "points" listesindeki her nokta çifti arasındaki öklid mesafesini hesaplayın
# bu mesafeleri "distances" adında başka bir listede saklayın

### MİNİMUM MESAFENİB BULUNMASI ###
# "distances" listesinden minimum mesafeyi bulun ve yazdırın

import math

points = [(5,34),(23,14),(8,11),(7,15),(12,6),(12,5)]

def euclideanDistance(first_point, second_point):
    
    x1, y1 = first_point
    x2, y2 = second_point

    return math.sqrt((x2 -x1) ** 2 + (y2 - y1) ** 2)

def return_points():
    for i in range(len(points)):
        print(points[i])
        for j in range(i+1, len(points)):
            print(points[j])
    return i, j

def main():
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)
    
    min_distance = min(distances)
    print(f"Minimum distance is {min_distance}")


if __name__ == "__main__":
    main()
