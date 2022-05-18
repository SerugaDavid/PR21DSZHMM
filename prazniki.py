def main():
    prazniki = [("01-01", "novo leto"),
                ("02-08", "Prešernov dan"),
                ("04-27", "dan upora proti okupatorju"),
                ("05-01", "praznik dela"),
                ("06-25", "dan državnosti"),
                ("08-15", "Marijino vnebovzetje"),
                ("09-31", "dan reformacije"),
                ("11-01", "dan spomina na mrtve"),
                ("12-25", "božič"),
                ("12-26", "dan samostojnosti in enotnosti")]
    leta = ["2020", "2021", "2022"]
    print("prazniki = [")
    for leto in leta:
        for praznik in prazniki:
            besedilo = str(praznik)
            print("('" + leto + "-" + besedilo[2:] + ",")
    print("]")


if __name__ == '__main__':
    main()
