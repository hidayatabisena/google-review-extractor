from random import randint


def generate_random_ip():
    return '.'.join(
        str(randint(0, 255)) for _ in range(4)
    )


a_list = []

for _ in range(9):
    a_list.append(generate_random_ip())


# 👇️ ['123.31.155.255', '70.22.71.106', '183.142.245.87']
print(a_list)

