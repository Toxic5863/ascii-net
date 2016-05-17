from input_font import glyphs
from keras_model import ocr, font_data


def test_keras_ocr():
    g = list(glyphs.default_glyphs())
    inputs, labels, chars = font_data.convert(g)

    m = ocr.Model(len(inputs[0]), len(labels[0]))

    for i in range(100):
        # train for 5 epochs
        m.train(inputs, labels, 5)

        # predict class for all training data
        p_classes = m.predict(inputs)

        # get wrongly predicted chars
        p_chars = font_data.deconvert(chars, p_classes)
        p_errors = [c for c, pc in zip(chars, p_chars) if c != pc]

        print('predict:', ''.join(p_chars))
        print('errors: ', ''.join(p_errors))

        if len(p_errors) == 0:
            break


if __name__ == "__main__":
    test_keras_ocr()
