
# Gradient Colors

Every file in this folder may only refer to 1 color key value  
the color you override must be in the top left, but can also fill the left side of the image  

the right side of the image can contain colors, gaps between colors are interpolated linearly  

a missing color at the beginning or end will cause a gradient between the key color and the gradient color  

The image's height is stretched to fit the height of whatever text is being styled, so colors in the gradient key may not entirely match what appears in the output texture  

multiple gradient rows can be defined in order to randomize the gradient across the text  
