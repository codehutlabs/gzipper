import argparse, gzip, os, shutil


def main():

    parser=argparse.ArgumentParser(
        description="""My Gzipper.""",
        epilog="""All's well that ends well.""")
    parser.add_argument('-f', '--filein', type=str, default=None, help='input file to gzip')
    parser.add_argument('-v', '--verbose', action="store_true", help='verbose mode')
    args=parser.parse_args()

    filein = None
    verbose = False

    if args.filein:
        filein = args.filein

    if args.verbose:
        verbose = True
        
    if os.path.isfile(filein):
        with open(filein, 'rb') as f_in:
            with gzip.open(filein + '.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        if verbose:
            print("File {} successfully gzipped.".format(filein))

    else:
        if verbose:
            print("File {} doesn't exist.".format(filein))

if __name__ == "__main__":
    main()
