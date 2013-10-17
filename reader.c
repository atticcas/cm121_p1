#include <stdlib.h>
#include <stdio.h>

int read_data(FILE *fp,
		int *id,
		double *prob_obs_unmut,
		double *prob_obs_mut)
{
	if(3 != fscanf(fp, "%d %lf %lf\n", id, prob_obs_unmut, prob_obs_mut)) {
		return EOF;
	}
	return 1;
}

int print_basic_score(FILE *fp, double score)
{
	if(1 != fprintf(fp, "BASIC_SCORE=%lf\n", score)) {
		return EOF;
	}
	return 1;
}

int print_adv_score(FILE *fp, double score)
{
	if(1 != fprintf(fp, "ADV_SCORE=%lf\n", score)) {
		return EOF;
	}
	return 1;
}

int print_logp(FILE *fp, double phi, double logp) {
	if(2 != fprintf(fp, "LOG_P_PHI %lf %lf\n", phi, logp)) {
		return EOF;
	}
	return 1;
}

int main(int argc, char *argv[])
{
	int id;
	double prob_obs_unmut, prob_obs_mut;
	double score, phi, logp;
	score = phi = logp = 0; // These need to be compute/
	while(EOF != read_data(stdin, &id, &prob_obs_unmut, &prob_obs_mut)) {
		//fprintf(stdout, "%d %lf %lf\n", id, prob_obs_unmut, prob_obs_mut);
		// We should check the return values below!:
		print_basic_score(stdout, score);
		print_adv_score(stdout, score);
		print_logp(stdout, phi, logp);
	}
}
