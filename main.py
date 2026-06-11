"""
main.py — RPPI Maroc master pipeline runner

Usage:
  python main.py                  # full pipeline
  python main.py --ingest         # Phase 3: scrape data
  python main.py --clean          # Phase 5: clean data

"""

import sys, os, argparse, warnings
warnings.filterwarnings("ignore")

sys.path.insert(0, os.path.dirname(__file__))

from database.models import init_db
from utils.logger import log


def run_full_pipeline():
    from ingestion.pipeline      import run_ingestion
    from processing.cleaner      import run_cleaning

    log.info("╔══════════════════════════════════════════╗")
    log.info("║   RPPI Maroc — Full Pipeline             ║")
    log.info("╚══════════════════════════════════════════╝")

    init_db()
    run_ingestion()
    run_cleaning()

    log.success("✅ Full pipeline ingest + cleaning complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RPPI Maroc Pipeline")
    parser.add_argument("--ingest",    action="store_true", help="Phase 3: scrape")
    parser.add_argument("--clean",     action="store_true", help="Phase 5: clean")
    args = parser.parse_args()

    init_db()

    if args.ingest:
        from ingestion.pipeline import run_ingestion
        run_ingestion()

    elif args.clean:
        from processing.cleaner import run_cleaning
        run_cleaning()


    else:
        run_full_pipeline()
