# computer-vision-project1
utd cs6384.002
What you need to implement
Most of your code should use OpenCV routines. You need to implement the two routines that do linear
stretching and class histogram equalization.
Input and output
All programs have the exact same arguments: an input image, window specification, and the name of the
output image. The window is specified in terms of the normalized coordinates w1, h1, w2, h2, where the
window upper left point is (w1, h1), and its lower right point is (w2, h2). For example, w1 = 0, h1 = 0,
w2 = 1, h2 = 1 is the entire image, and w1 = 0.3, h1 = 0.3, w2 = 0.7, h2 = 0.7 is a window in the center of
the image. The provided example program shows how to read the arguments and go over the pixels of the
specified window.
1
Evaluation
Your grade will depend on the following two components: correctness of your programs and your report of
results of experiments. You are asked to experiment with your programs and report the following:
1. Describe strange behavior when colors appear to be changing. If this occurs it is an indication that the
OpenCv code does not handle out of range values properly. You should report it and show an image
where this occurs.
2. Among the 3 lscl programs decide which one is the best and which one is the worst. Show images that
support your conclusion.
3. Among the 6 histeq programs decide which one is the best and which one is the worst. Show images that
support your conclusion.
All experiments should be done with natural images and a window size of at least 50 × 50.
What you need to submit
• Submit the source code of all your programs.
• Submit a report of your experiments.
• Submit at least 3 and at most 10 images to justify the conclusions in your report. Make sure that
these images are unique to your project by keeping them private. They cannot be used in any other
project. (You will lose points if the pictures you submit appear in another project.)
