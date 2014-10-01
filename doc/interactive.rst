Interactive Viewing
===================

Introduction
------------

To run the viewer in stand-alone mode, you need ipython.  Start
ipython with::

  ipython -q4thread

The ccad viewer uses qt; that's why you use the -q4thread option.

Now, from the ipython prompt, you can work with ccad interactively.
Try this::

  In [1]: import ccad.model as cm
  In [2]: import ccad.display as cd
  In [3]: s1 = cm.sphere(1.0)
  In [4]: s2 = cm.box(1.0, 2.0, 3.0)
  In [5]: s2.translate((2.0, 0.0, 0.0))
  In [6]: v1 = cd.view()

After the last line, you should see a window appear with nothing in
it.  **v1** is an instance of a viewing window.  Now type::

  In [7]: v1.display(s1)

You should see **s1** in your window.  Move to the window, hold on the
middle mouse button and pan.  You should see the shape moving.  Now,
go back to the ipython prompt and type::

  In [8]: v1.display(s2)

You'll see **s2** appear in the viewer.

To clear the window, use::

  In [9]: v1.clear()

You have interactive viewing.

Now, start a second window with::

  In [10]: v2 = cd.view()

**v2** is an instance of the second displayed window.  Add something
different to it::

  In [11]: v2.display(cm.cone(4.0, 2.0, 2.0))

Note that each viewer is independent.  You may create as many view
windows as you like.
