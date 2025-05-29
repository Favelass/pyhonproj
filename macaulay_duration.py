def macaulay_duration(coupon_rate, face_value, ytm, n):
    C = coupon_rate * face_value
    y = ytm
    PV_total = 0
    weighted_sum = 0

    for t in range(1, n + 1):
        cash_flow = C if t < n else C + face_value
        pv = cash_flow / (1 + y)**t
        PV_total += pv
        weighted_sum += t * pv

    duration = weighted_sum / PV_total
    return round(duration, 4), round(PV_total, 2)

# Input Parameters
face_value = 1000
coupon_rate = 0.058
n_years = 3

# Case 1: YTM = 5.8%
duration_58, price_58 = macaulay_duration(coupon_rate, face_value, 0.058, n_years)

# Case 2: YTM = 8%
duration_80, price_80 = macaulay_duration(coupon_rate, face_value, 0.08, n_years)

# Output the results
print("=== Macaulay Duration and Price Comparison ===")
print(f"YTM 5.8% -> Duration: {duration_58} years | Price: ${price_58}")
