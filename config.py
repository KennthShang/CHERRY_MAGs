import  argparse

args = argparse.ArgumentParser()
args.add_argument('--dataset', default='virus-host')
args.add_argument('--learning_rate', type=float, default=0.001)
args.add_argument('--model', type=str, default = 'pretrain')
args.add_argument('--mode', type=str, default = 'virus')
args.add_argument('--gpus', type=int, default = 0)
args.add_argument('--topk', type=int, default = 1)
args.add_argument('--t', type=float, default = 0.5)

inputs = args.parse_args()
print(inputs)