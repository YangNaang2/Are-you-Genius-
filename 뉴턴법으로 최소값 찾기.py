def function(x):
    return 3 + 6*x + 5*x**2 + 3*x**3 + 4*x**4

def derivative_first(x, h=0.01):
    return (function(x + h*x) - function(x - h*x)) / (2 * h * x)

def derivative_second(x, h=0.01):
    return (function(x + h*x) - 2*function(x) + function(x - h*x)) / (h*x)**2

def newton_raphson(x0, tolerance=0.01, max_iterations=100):
    x = x0
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        df_dx = derivative_first(x)
        d2f_dx2 = derivative_second(x)
        error = abs(df_dx / d2f_dx2)
        x -= df_dx / d2f_dx2
        
        print("Iteration {}: x = {:.4f}, f(x) = {:.4f}, f'(x) = {:.4f}, f''(x) = {:.4f}, Error = {:.6f}".format(
            iteration, x, function(x), df_dx, d2f_dx2, error))
        
        if error < tolerance:
            break
    
    return x

# 초기값 x0 = -1로 설정
initial_x = -1

# Newton-Raphson을 사용하여 최솟값 계산
minimum_value = newton_raphson(initial_x)

print("\n최솟값 x: {:.4f}".format(minimum_value))
print("최솟값 f(x): {:.4f}".format(function(minimum_value)))
