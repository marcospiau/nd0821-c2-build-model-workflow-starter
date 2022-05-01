#!/usr/bin/env python
"""
Download from W&B the raw dataset and apply some basic data cleaning, exporting the result to a new artifact
"""
import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    logging.info(f'Loading artifact %s', args.input_artifact)
    artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################
    df = pd.read_csv(artifact_local_path)
    logger.info('Filtering prices between %f and %f', args.min_price,
            args.max_price)
    df = df[df['price'].between(args.min_price, args.max_price)].copy()
    logger.info("Converting 'last_review' column do datetime type")
    df['last_review'] = pd.to_datetime(df['last_review'])
    logger.info('Saving dataframe in clean_sample.csv')
    df.to_csv("clean_sample.csv", index=False)
    
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )
    artifact.add_file("clean_sample.csv")
    logger.info('Uploading artifact to wandb')
    run.log_artifact(artifact)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")


    parser.add_argument(
        "--input_artifact", 
        type=str,
        help='Input artifact name',
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help='Output artifact name',
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help='Output type',
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help='Output description',
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help='Minimum price for an example to be kept on dataset',
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help='Maximum price for an example to be kept on dataset',
        required=True
    )


    args = parser.parse_args()

    go(args)
