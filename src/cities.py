#!/usr/bin/env python3

import pandas as pd

def cities():
    cities = ["Helsinki", "Espoo", "Tampere", "Vantaa", "Oulu"]
    population = [643272, 279044, 231853, 223027, 201810]
    area = [715.48, 528.03, 689.59, 240.35, 3817.52]

    # make the rows named by city
    data = {
        "Population": population,
        "Total area": area
    }

    df = pd.DataFrame(data, index=cities)
    return df

def main():
    print(cities())
    
if __name__ == "__main__":
    main()
