from recommenders.distance_based_recommender import DistanceBasedRecommender
import run.cf
import data.data as data
import utils.log as log


rp3beta = DistanceBasedRecommender.SIM_RP3BETA

ks = [100, 200, 300]
alphas = [0.25, 0.5, 0.75]
betas = [0.25, 0.5, 0.75]
shrinks = [50, 80, 100, 150]

with open('validation_results/cf_base_rp3beta.txt', 'w') as file:
    for k in ks:
        for a in alphas:
            for b in betas:
                for shrink in shrinks:
                    recs, map10 = run.cf.run(distance=rp3beta, k=k, shrink=shrink, alpha=a, beta=b, verbose=False)
                    logmsg = 'MAP: {} \tknn: {} \ta: {} \tb: {} \tshrink: {}\n'.format(map10,k,a,b,shrink)
                    log.warning(logmsg)
                    file.write(logmsg)
