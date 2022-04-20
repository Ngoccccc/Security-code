import gmpy2
from gmpy2 import mpz, isqrt, f_mod, mul, t_div
n = mpz('720062263747350425279564435525583738338084451473999841826653057981916355690188337790423408664187663938485175264994017897083524079135686877441155132015188279331812309091996246361896836573643119174094961348524639707885238799396839230364676670221627018353299443241192173812729276147530748597302192751375739387929')
r = isqrt(mul(n, 24))

b = r if pow(r, 2) == (mul(n, 24)) else r + 1
x  = isqrt(pow(b, 2) - 24 * n)

p_tmp = b - x
q_tmp = b + x

if f_mod(p_tmp, 6) == 0 and f_mod(q_tmp, 4) == 0:
    p = min(t_div(p_tmp, 6), t_div(q_tmp, 4))
    q = max(t_div(p_tmp, 6), t_div(q_tmp, 4))
elif f_mod(p_tmp, 4) == 0 and f_mod(q_tmp, 6) == 0:
    p = min(t_div(p_tmp, 4), t_div(q_tmp, 6))
    p = max(t_div(p_tmp, 4), t_div(q_tmp, 6))

print("P: \n{}".format(p))
print("Q: \n{}".format(q))


