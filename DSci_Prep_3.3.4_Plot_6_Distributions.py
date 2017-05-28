"""
Dependencies: Uses ffmpeg to convert pngs to quicktime movies. ffmpeg can be tricky to install
"""
import os
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

THINK_DIR = "/Users/twaddy/NOTES/thinkful/DataSciBootCampPrep/"
PRESENT_DIR = os.path.join(THINK_DIR, 'assignment_presentation','sample_6_distributions')
FONT_PATH = os.environ.get("FONT_PATH", "/Library/Fonts/Times New Roman.ttf")

print("\n{0}\nSampling into 6 different distributions and plotting histograms of the results.\n{0}\n".format("*"*60))
beta_slate_text = "The Beta Distribution:\n" \
                  "    ...a special case of the Dirichlet distribution,\n" \
                  "    and is related to the Gamma distribution.\n\n" \
                  "It is often seen in Bayesian inference and order statistics."


chisquared_slate_text = "The ChiSquared Distribution:\n" \
                        "When df independent random variables, each with standard normal\n" \
                        "distributions (mean 0, variance 1), are squared and summed,\n" \
                        "the resulting distribution is chi-square (see Notes).\n\n" \
                        "This distribution is often used in hypothesis testing.\n"

gamma_slate_text = "The Gamma Distribution:\n " \
                   "Samples drawn from Gamma distribution with specified parameters\n," \
                   "shape (often designated “k”) and scale (often designated “theta”),\n " \
                   "where both parameters are > 0.\n\n" \
                   "Often used to model the times to failure of electronic components,\n" \
                   "and arises naturally in processes for which the waiting times between\n " \
                   "Poisson distributed events are relevant.\n"

laplace_slate_text = "The Laplace Distribution:\n " \
                     "The Laplace distribution (or double exponential dist) is similar to\n" \
                     "the Gaussian/normal dist, but sharper at peak and has fatter tails.\n" \
                     "It represents the difference between two independent,\n" \
                     "identically distributed exponential random variables.\n\n" \
                     "" \
                     "The first law of Laplace, from 1774, states that\n" \
                     "the frequency of an error can be expressed as an exponential function of the\n" \
                     "absolute magnitude of the error, which leads to the Laplace distribution.\n" \
                     "For many problems in economics and health sciences, this distribution\n" \
                     "seems to model the data better than the standard Gaussian distribution.\n"

rayleigh_slate_text = "The Rayleigh Distribution:\n" \
                      "The chi and Weibull distributions are generalizations of the Rayleigh.\n\n"\
                      "The Rayleigh distribution would arise, for example:\n" \
                      "if the East and North components of wind velocity had identical zero-mean\n"\
                      "Gaussian distributions. Then wind speed would have a Rayleigh distribution.\n\n"\
                      "Wave heights tend to follow a Rayleigh distribution\n" \


pareto_slate_text = "The Pareto Distribution:\n" \
                    "The Lomax or Pareto II distribution is a shifted Pareto distribution.\n\n"\
                    "The Pareto distribution must be greater than zero, and is unbounded above.\n "\
                    "It is also known as the “80-20 rule”. In this distribution, 80 percent of\n "\
                    "the weights are in the lowest 20 percent of the range,\n "\
                    "while the other 20 percent fill the remaining 80 percent of the range.\n\n"\
                    "" \
                    "Outside economics it is generally referred to as the Bradford distribution.\n " \
                    "Italian economist Vilfredo Pareto developed the distribution to describe the\n " \
                    "distribution of wealth in an economy. It has also found use in insurance,\n " \
                    "web page access statistics, oil field sizes, and many other problems,\n " \
                    "including the download frequency for projects in Sourceforge [R251].\n " \
                    "It is one of the so-called “fat-tailed” distributions.\n"




def make_slate_png(img_dir=None, slate_text=None, do_link=False, do_preview=False):
    slate_png = os.path.join(img_dir, 'slate.png')
    img = Image.new('RGB', (640, 480))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, 18)

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((640/12, 480/6), "{0}".format(slate_text), (255, 255, 255), font=font)
    img.save(slate_png)
    if do_preview:
        os.system("open -a preview {0}".format(slate_png))
    if do_link:
        slate_link = os.path.join(img_dir, 'presentation.0.png')
        os.system("ln -f -s {0} {1}".format(slate_png, slate_link))
# make_slate_png(img_dir=PRESENT_DIR, slate_text=beta_slate_text, do_link=True, do_preview=False)


def wedge_beta(start=1, end=100, step=5, do_link=False):
    ii = 0
    aa = 10
    for bb in range(start, end + 1, step):
        ii += 1
        print(ii, aa, bb)

        beta_var = np.random.beta(a=aa, b=bb, size=100)
        # Plot a histogram.
        plt.hist(beta_var)
        plt.title("Beta Distribution, a = {0}, b = {1}".format(aa, bb))
        plt.ylabel('Count')
        plt.xlim([0, 1])
        plt.ylim([0, 50])
        plt.tight_layout()
        beta_png_fp   = os.path.join(PRESENT_DIR, 'dist_beta_a_{0}__b_{1}.png'.format(aa, bb))
        beta_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(beta_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(beta_png_fp, beta_png_link))
    bb = 10
    for aa in range(start ,end + 1, step):
        ii += 1
        print(ii, aa, bb)

        beta_var = np.random.beta(a=aa, b=bb, size=100)
        plt.hist(beta_var)
        plt.title("Beta Distribution, a = {0}, b = {1}".format(aa, bb))
        plt.ylabel('Count')
        plt.xlim([0, 1])
        plt.ylim([0, 50])
        plt.tight_layout()
        beta_png_fp   = os.path.join(PRESENT_DIR, 'dist_beta_a_{0}__b_{1}.png'.format(aa, bb))
        beta_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(beta_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(beta_png_fp, beta_png_link))



def wedge_chisquared(start=1, end=100, step=1, do_link=False):
    for ii in range(start, end + 1, step):
        df = ii/10
        print(ii, df)
        chisquared_var = np.random.chisquare(df, size=100)
        plt.hist(chisquared_var)
        plt.title("ChiSquared Distribution, df = {0}".format(df))
        plt.ylabel('Count')
        plt.xlim([0, 20])
        plt.ylim([0, 100])
        plt.tight_layout()
        chisquared_png_fp   = os.path.join(PRESENT_DIR, 'dist_chisquared_df{0}.png'.format(df))
        chisquared_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(chisquared_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(chisquared_png_fp, chisquared_png_link))


def wedge_gamma(start=1, end=100, step=5, do_link=False):
    ii = 0
    shape = 0.2
    for jj in range(start, end + 1, step):
        theta = jj/10.0
        ii += 1
        print(ii, shape, theta)

        gamma_var = np.random.gamma(shape=shape, scale=theta, size=100)
        plt.hist(gamma_var)
        plt.title("Gamma Distribution, shape(k) = {0}, scale(theta) = {1}".format(shape, theta))
        plt.ylabel('Count')
        plt.xlim([0, 100])
        plt.ylim([0, 100])
        plt.tight_layout()
        gamma_png_fp   = os.path.join(PRESENT_DIR, 'dist_gamma_k_{0}__theta{1}.png'.format(shape, theta))
        gamma_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(gamma_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(gamma_png_fp, gamma_png_link))

    theta = 5.0
    for jj in range(start, end + 1, step):
        shape = jj/10.0
        ii += 1
        print(ii, shape, theta)

        gamma_var = np.random.gamma(shape=shape, scale=theta, size=100)
        plt.hist(gamma_var)
        plt.title("Gamma Distribution, shape(k) = {0}, scale(theta) = {1}".format(shape, theta))
        plt.ylabel('Count')
        plt.xlim([0, 100])
        plt.ylim([0, 100])
        plt.tight_layout()
        gamma_png_fp   = os.path.join(PRESENT_DIR, 'dist_gamma_k_{0}__theta_{1}.png'.format(shape, theta))
        gamma_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(gamma_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(gamma_png_fp, gamma_png_link))



def wedge_laplace(start=1, end=100, step=5, do_link=False, do_axis_limits=True):
    ii = 0
    loc = 300
    for scale in range(start, end + 1, step):
        ii += 1
        print(ii, loc, scale)

        laplace_var = np.random.laplace(loc=loc, scale=scale, size=100)
        # Plot a histogram.
        plt.hist(laplace_var)
        plt.title("Laplace Distribution, loc = {0}, scale = {1}".format(loc, scale))
        plt.ylabel('Count')
        if do_axis_limits:
            plt.xlim([0, 800])
            plt.ylim([0, 60])
        plt.tight_layout()
        laplace_png_fp   = os.path.join(PRESENT_DIR, 'dist_laplace_loc_{0}__scale_{1}.png'.format(loc, scale))
        laplace_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(laplace_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(laplace_png_fp, laplace_png_link))


def wedge_rayleigh(start=1, end=100, step=1, do_link=False, do_axis_limits=False):
    ii = 0
    for chi in range(start, end + 1, step):
        ii += 1
        print(ii,chi)
        rayleigh_var = np.random.rayleigh(chi, size=100)
        plt.hist(rayleigh_var)
        plt.title("Rayleigh Distribution, chi = {0}".format(chi))
        plt.ylabel('Count')
        if do_axis_limits:
            plt.xlim([0, 300])
            plt.ylim([0, 30])
        plt.tight_layout()
        rayleigh_png_fp   = os.path.join(PRESENT_DIR, 'dist_rayleigh_chi{0}.png'.format(chi))
        rayleigh_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(rayleigh_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(rayleigh_png_fp, rayleigh_png_link))


def wedge_pareto(start=1, end=100, step=1, do_link=False, do_axis_limits=False):
    ii = 0
    for a in range(start, end + 1, step):
        ii += 1
        print(ii, a)
        pareto_var = np.random.pareto(a, size=100)
        plt.hist(pareto_var)
        plt.title("Pareto Distribution, a(scale) = {0}".format(a))
        plt.ylabel('Count')
        if do_axis_limits:
            if a < 5:
                plt.xlim([0, 10])
            else:
                plt.xlim([0, 1])
            plt.ylim([0, 80])
        plt.tight_layout()
        pareto_png_fp   = os.path.join(PRESENT_DIR, 'dist_pareto_a{0}.png'.format(a))
        pareto_png_link = os.path.join(PRESENT_DIR, 'presentation.{0:04d}.png'.format(ii))
        plt.savefig(pareto_png_fp)
        plt.cla()
        plt.clf()
        if do_link:
            os.system("ln -f -s {0} {1}".format(pareto_png_fp, pareto_png_link))


def make_movie(in_dir=None, out_mov_root=None, do_play_movie=True, do_png_cleanup=False):
    cd_cmd = "cd {0}".format(in_dir)
    out_mov_fp = out_mov = os.path.join(in_dir, '{0}.mov'.format(out_mov_root))
    ffm_cmd = "{0}; ffmpeg " \
              "-f image2 " \
              "-pattern_type glob " \
              "-framerate 12 " \
              "-i 'presentation.*.png' " \
              "-s 640x480 " \
              "-vcodec libx264 " \
              "-crf 25 " \
              "-y " \
              "-pix_fmt yuv420p {1}".format(cd_cmd, out_mov_fp)
    subprocess.call(ffm_cmd, shell=True)
    if do_play_movie:
        os.system("open -a /Applications/QuickTime\ Player.app {0}".format(out_mov_fp))
    if do_png_cleanup:
        os.system("rm {0}/*.png".format(in_dir))


# make_slate_png(img_dir=PRESENT_DIR, slate_text=beta_slate_text, do_link=True, do_preview=False)
# wedge_beta(do_link=True)
# make_movie(in_dir=PRESENT_DIR, out_mov_root="Beta")

# make_slate_png(img_dir=PRESENT_DIR, slate_text=chisquared_slate_text, do_link=True, do_preview=False)
# wedge_chisquared(do_link=True)
# make_movie(in_dir=PRESENT_DIR, out_mov_root="ChiSquared")

# make_slate_png(img_dir=PRESENT_DIR, slate_text=gamma_slate_text, do_link=True, do_preview=False)
# wedge_gamma(do_link=True)
# make_movie(in_dir=PRESENT_DIR, out_mov_root="Gamma")

# make_slate_png(img_dir=PRESENT_DIR, slate_text=laplace_slate_text, do_link=True, do_preview=False)
# wedge_laplace(do_link=True, do_axis_limits=True)
# make_movie(in_dir=PRESENT_DIR, out_mov_root="Laplace", do_png_cleanup=True)

# make_slate_png(img_dir=PRESENT_DIR, slate_text=rayleigh_slate_text, do_link=True, do_preview=False)
# wedge_rayleigh(do_link=True, do_axis_limits=True)
# make_movie(in_dir=PRESENT_DIR, out_mov_root="Rayleigh", do_png_cleanup=True)

make_slate_png(img_dir=PRESENT_DIR, slate_text=pareto_slate_text, do_link=True, do_preview=False)
wedge_pareto(do_link=True, do_axis_limits=True)
make_movie(in_dir=PRESENT_DIR, out_mov_root="Pareto", do_png_cleanup=True)



