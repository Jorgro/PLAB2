from cyphers import Caesar, Multiplicative, Affine, Unbreakable, RSA
from person import Sender, Receiver, Hacker


def __main__():
    text = "HELLO THERE! GENERAL KENOBI, YOU ARE A BALD ONE!"

    # Tester caesar:

    print("\nTesting Caesar:")
    sender = Sender(Caesar())
    sender.set_key(93)

    receiver = Receiver(Caesar())
    receiver.set_key(93)

    encoded = sender.operate_cipher(text)
    print("Encoded message:", encoded)

    decoded = receiver.operate_cipher(encoded)
    print("Decoded message:", decoded)

    print("Verify: ", Caesar.verify("HELLO", 3))

    # Tester multiplicative:

    print("\nTesting Multiplicative:")
    sender = Sender(Multiplicative())
    sender.set_key(93)

    receiver = Receiver(Multiplicative())
    receiver.set_key(93)

    encoded = sender.operate_cipher(text)
    print("Encoded message:", encoded)

    decoded = receiver.operate_cipher(encoded)
    print("Decoded message:", decoded)

    print("Verify: ", Multiplicative.verify("HELLO", 2))

    # Tester affine:

    print("\nTesting Affine:")
    sender = Sender(Affine())
    sender.set_key((3, 2))

    receiver = Receiver(Affine())
    receiver.set_key((3, 2))

    encoded = sender.operate_cipher(text)
    print("Encoded message:", encoded)

    decoded = receiver.operate_cipher(encoded)
    print("Decoded message:", decoded)

    print("Verify: ", Affine.verify("HELLO", (3, 2)))

    # Tester unbreakable:

    print("\nTesting Unbreakable:")
    sender = Sender(Unbreakable())
    sender.set_key("PIZZA")

    receiver = Receiver(Unbreakable())
    receiver.set_key("PIZZA")

    encoded = sender.operate_cipher(text)
    print("Encoded message:", encoded)

    decoded = receiver.operate_cipher(encoded)
    print("Decoded message:", decoded)

    print("Verify: ", Unbreakable.verify("HELLO", "PIZZA"))

    # Tester RSA:

    print("\nTesting RSA:")

    keys = RSA.generate_keys()
    sender = Sender(RSA())
    sender.set_key(keys[0])

    receiver = Receiver(RSA())
    receiver.set_key(keys[1])

    encoded = sender.operate_cipher(text)
    print("Encoded message:", encoded)

    decoded = receiver.operate_cipher(encoded)
    print("Decoded message:", decoded)

    print("Verify: ", RSA.verify("HELLO", keys))

    print("\nTesting the hacker:")
    msg = Multiplicative.encode("PICKAXE JURGEN", 3)
    print(Hacker().operate_cipher(msg))

__main__()
