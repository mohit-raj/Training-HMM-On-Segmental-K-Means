import train

def main ():
    model = train.Train (5)
    model.load_data("../data/day.csv")
    # print(model.observation)
    model.get_observation()
    model.get_segments()

if __name__ == "__main__":
    main()
