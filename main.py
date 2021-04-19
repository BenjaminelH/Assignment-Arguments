# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#part 1
Ben = '<name>'

def greet(name: str, template: str = f'Hello, {Ben}!'):
          return template.replace(Ben, name)

if __name__ == '__main__':
    print(greet('Doc'))
    print(greet('Bob', 'Whats up, <name>!'))

#part2
Gravities = {
'sun': 274.0,
'jupiter': 24.9,
'neptune': 11.2,
'saturn': 10.4,
'earth': 9.8,
'uranus': 8.9,
'venus': 8.9,
'mars': 3.7,
'mercury': 3.7,
'moon': 1.6,
'pluto': 0.6
}


def force(mass: float, body: str = 'earth'):
    if body not in Gravities:
        return None 
    return mass * Gravities[body]


if __name__ == '__main__':
    print(force(1, 'earth'))

#part3
G = 6.674 * 10 ** -11


def pull(m1: float, m2: float, d: float):
    return G * m1 * m2 / (d ** 2)


if __name__ == '__main__':
    print(pull(1000, 11000000, 2))
