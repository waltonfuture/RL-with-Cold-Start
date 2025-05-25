set -x

MODEL_PATH=Qwen/Qwen2.5-VL-7B-Instruct # replace with your model path (after the cold start)

python3 -m verl.trainer.main \
    config=examples/config.yaml \
    data.train_files=WaltonFuture/Multimodal-RL-Data@train \
    data.val_files=hiyouga/geometry3k@test \
    worker.actor.model.model_path=${MODEL_PATH} \
    trainer.experiment_name=qwen2_5_vl_7b_grpo \
    trainer.n_gpus_per_node=8 \
    data.val_batch_size=500 \
    data.max_pixels=1204224 \
    trainer.total_episodes=2 \
    trainer.save_limit=7 \
    worker.reward.score_function=./examples/score_function/math.py:compute_score \

