import math
# Расчет барботажа
q_n = 10/ 86400#float (input ("q_n="))  # дебит по нефти
D = 137 / 1000 #float (input("D="))  #диаметр ЭК
mu_n = 3* 1e-3#float (input("mu="))  #вязкость нефти
ro_n =780 #float (input ("ro_n=")) #плотность нефти
# ************(для КРД)
ro_w = 1010 #float(input("ro_w")) #плотность воды
bhp = 10* 10**6 #float(input("bhp="))  #BHP
H_0 = 1500 #float(input("H_0=")) #глубина спуска НКТ
d = 73/1000#float(input("d=")) #d НКТ
p_nas =10* 10**6 #float(input("p_nas="))  #давление насыщения
H_well = 2000 #float (input("H_well=")) #глубина скважины
G0 = 270 #float(input("G0=")) #GOR
ro_g = 1#float(input("ro_g=")) #плотность газа(попутного)
z = 1#float(input("z=")) #коэффициент сжимаемости
P0 = 10**5 #Pa
sigma =20*1e-3#float(input("sigma=")) #поверхност9ное натяжение
mu_lg = 2* 1e-3 #float(input("mu_water="))  #поверхностное натяжение жидкость газ
d_bbl = 0.0034 # диаметр пузырька  привет от Рината
#******
p = bhp
H = H_well
i = 0
a = []
pp = []
while H > H_0:
    p_sr = p - 0.25  # при этом давление вычисляются параметры движения(параметры постоянные)

    Re = 1.274 * q_n / D / mu_n * ro_n
    if Re > 400:  # относительной скоростью можно пренебречь
        fi = 0.915 + Re / 10000
    else:
        fi = 0.0024 * Re
    ro_wn = ro_w * (1 - fi) + fi * ro_n
    if p > p_nas:
        ro = ro_wn
    if p <=  p_nas : #учитывается газ
        if Re > 850 :
            print("происходит вынос воды")
            break
        else:

            Vn = float(G0 * q_n * z * P0 / p)
            v0 = 0.42 * 9.81 * (ro_wn - ro_g) * (d_bbl ** 2) * math.pow(Vn / math.pi * (D**2) / 4 / sigma / mu_lg ** 3, 0.25)
            ro = ro_wn * (1 - Vn / v0 * (1 - ro_g / ro_wn))

    p = p - 0.5 * 10**6
    dH = 5 / ro / 9.81 * 10**5
    print(H)
    H = H - dH
    print(H)
    a.insert(i, H)
    pp.insert(i,p)
    i += 1
print(a)










