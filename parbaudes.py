def lasit_sauli():
    pass
    try:
        with open ("teksts.txt", 'r', encoding='utf8') as sauli:
            saturs=sauli.read()
            print(type(saturs))
            print(saturs)
    except FileNotFoundError:
        print("Milana Radomska")

if __name__=="__main__":
 lasit_sauli()