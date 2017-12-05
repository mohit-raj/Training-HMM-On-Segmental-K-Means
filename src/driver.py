import segmentalKMeans import SegmentalKMeans

def main ():
    model = SegmentalKMeans ('../data/day.csv', 10, 5)

    training_sequences = model.get_segments ()
    print (training_sequences)

if __name__ == "__main__":
    main()
