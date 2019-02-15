from acme import Product
import numpy as np
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def pick_random_name():
    n_a = np.random.randint(0, 5)
    n_n = np.random.randint(0, 5)
    print(n_a, n_n)
    return ADJECTIVES[n_a] + " " + NOUNS[n_n]


def generate_products(n=30):
    product_list = []
    for i in range(0, n):
        product_name = pick_random_name()
        price = np.random.randint(5, 101)
        weight = np.random.randint(5, 101)
        fammability = np.random.uniform(0.0, 2.5)
        p = Product(product_name, price, weight, fammability)
        product_list.append(p)
    return product_list


def inventory_report(prodcut_list):
    prices = [p.price for p in prodcut_list]
    weights = [p.weight for p in prodcut_list]
    flamm = [p.flammability  for p in prodcut_list]
    unique_product_names = set([p.name for p in prodcut_list])
    n_unique_name = len(unique_product_names)
    ave_price = np.mean(prices)
    ave_weight = np.mean(weights)
    ave_fammability = np.mean(flamm)
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print("Unique product names:", n_unique_name)
    print("Average price:", ave_price)
    print("Average weight:", ave_weight)
    print("Average flammability: ", ave_fammability)


if __name__ == '__main__':
    inventory_report(generate_products())
