import ccad.model as cm
import ccad.display as cd


def main():
    s1 = cm.sphere(1.0)
    s2 = cm.box(1.0, 2.0, 3.0)
    s2.translate((2.0, 0.0, 0.0))
    v1 = cd.view()
    v1.display(s1)
    v1.display(s2)
    cd.start()

if __name__ == '__main__':
    main()
