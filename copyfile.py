import os
import shutil
import argparse

parser = argparse.ArgumentParser(description='copyfile --sdir sourecdir --dir destdir')
parser.add_argument('--sdir', type=str, default=".",   help='source directory',required=False)
parser.add_argument('--ddir', type=str, default="dest", help='dest directory',required=False)

args = parser.parse_args()

listfiles=[
    ["com.unity.ml-agents/Runtime/","Academy.cs"],
    ["com.unity.ml-agents/Runtime/","Agent.cs"],
    ["com.unity.ml-agents/Runtime/Communiticator/","RpcCommunicator.cs"],
    ["ml-agents/ml-agents/mlagents/trainers/","agent_processor.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","base_env.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","communicator.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","environment.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","exception.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","rpc_communicator.py"],
    ["ml-agents/ml-agents-env/mlagents_envs/","rpc_utils.py"],
    ["ml-agents/protobf-deffinitions/proto/mlagents_envs/communicator_objects/","environment_statistics.proto"],
    ["ml-agents/protobf-deffinitions/proto/mlagents_envs/communicator_objects/","unity_rl_output.proto"],
    ["Project/Assets/ML-Agents/Examples/FoodCollector/Scripts/","FoodCollectorAgent.cs"],
    ["Project/Assets/ML-Agents/Examples/FoodCollector/Scripts/","FoodCollectorSettings.cs"]
    ]


def copyFromTo(sdir,ddir):
    for (fdname,fname) in listfiles:
        sfname = f"{sdir}/{fdname}{fname}"
        dfname = f"{ddir}/{fdname}{fname}"
        dddir = f"{ddir}/{fdname}"
        if not os.path.exists(dddir):
            print(f"Creating directory {dddir}")
            os.makedirs(dddir)
        print(f"copy from {sfname} to {dfname}")
        shutil.copyfile(sfname,dfname)

copyFromTo(args.sdir,args.ddir)