#!/bin/bash
# see weblate/weblate/examples/celery

export CELERY_APP=weblate.utils

cd $HOME/weblate
. .venv/bin/activate

python -m celery multi stop \
    notify memory celery backup translate \
    --pidfile=$HOME/var/run/weblate-%n.pid \
    --logfile=$HOME/var/log/weblate-%n%I.log --loglevel=DEBUG \
    --beat:celery --queues:celery=celery --prefetch-multiplier:celery=4 \
    --queues:notify=notify --prefetch-multiplier:notify=10 \
    --queues:memory=memory --prefetch-multiplier:memory=10 \
    --queues:translate=translate --prefetch-multiplier:translate=4 \
    --concurrency:backup=1 --queues:backup=backup  --prefetch-multiplier:backup=2
