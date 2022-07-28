import sys
import models
import serializer


def main():
    args = sys.argv
    models.collection1.add(models.Card(
        int(args[1]),
        int(args[2]),
        args[3],
        args[4],
        args[5],
        args[6],
        {args[7]: int(args[8])}
    ))
    serializer.serialize_collection(models.collection1.dict())


if __name__ == '__main__':
    main()
