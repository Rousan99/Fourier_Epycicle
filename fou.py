from Fourier_Calculation import *

time_table, x_table, y_table = create_close_loop('rex.jpg')
coef = coef_list(time_table, x_table, y_table)
print(coef)
space = np.linspace(0, 2*pi,300)
x_DFT = [DFT(t, coef)[0] for t in space]
y_DFT = [DFT(t, coef)[1] for t in space]
fig, ax = plt.subplots(figsize=(5, 5))
ax.plot(x_DFT, y_DFT,c='blue')
ax.plot(x_table, y_table,c='blue')
ax.set_aspect('equal', 'datalim')
xmin, xmax = xlim()
ymin, ymax = ylim()
anim = visualize(x_DFT, y_DFT, coef, space, [xmin, xmax, ymin, ymax],'T-Rex')
#Writer = animation.writers['ffmpeg']
#writer = Writer(fps=30)
#anim.save('rex.mp4',writer=writer, dpi=150)
#Previous 3 are comment-out as all people don't have ffmpeg
plt.style.use('dark_background')
plt.show()
