"""
Templates for slurm.conf and slurmdbd.conf
"""

slurm_conf_template = """
# slurm.conf file generated by configurator.html.
# Put this file on all nodes of your cluster.
# See the slurm.conf man page for more information.
#
ControlMachine=%(master)s
#ControlAddr=
#BackupController=
#BackupAddr=
# 
AuthType=auth/munge
CacheGroups=0
#CheckpointType=checkpoint/none 
CryptoType=crypto/munge
#DisableRootJobs=NO 
#EnforcePartLimits=NO 
#Epilog=
#EpilogSlurmctld= 
#FirstJobId=1 
#MaxJobId=999999 
#GresTypes= 
#GroupUpdateForce=0 
#GroupUpdateTime=600 
#JobCheckpointDir=/var/slurm/checkpoint 
#JobCredentialPrivateKey=
#JobCredentialPublicCertificate=
#JobFileAppend=0 
#JobRequeue=1 
#JobSubmitPlugins=1 
#KillOnBadExit=0 
#Licenses=foo*4,bar 
#MailProg=/bin/mail 
#MaxJobCount=5000 
#MaxStepCount=40000 
#MaxTasksPerNode=128 
MpiDefault=none
#MpiParams=ports=#-# 
#PluginDir= 
#PlugStackConfig= 
#PrivateData=jobs 
ProctrackType=proctrack/linuxproc
#Prolog=
#PrologSlurmctld= 
#PropagatePrioProcess=0 
#PropagateResourceLimits= 
#PropagateResourceLimitsExcept= 
ReturnToService=1
#SallocDefaultCommand= 
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmctldPort=6817
SlurmdPidFile=/var/run/slurmd.pid
SlurmdPort=6818
SlurmdSpoolDir=/tmp/slurmd
SlurmUser=root
#SlurmdUser=root 
#SrunEpilog=
#SrunProlog=
StateSaveLocation=/tmp
SwitchType=switch/none
#TaskEpilog=
TaskPlugin=task/none
#TaskPluginParam=
#TaskProlog=
#TopologyPlugin=topology/tree 
#TmpFs=/tmp 
#TrackWCKey=no 
#TreeWidth= 
#UnkillableStepProgram= 
#UsePAM=0 
# 
# 
# TIMERS 
#BatchStartTimeout=10 
#CompleteWait=0 
#EpilogMsgTime=2000 
#GetEnvTimeout=2 
#HealthCheckInterval=0 
#HealthCheckProgram= 
InactiveLimit=0
KillWait=30
#MessageTimeout=10 
#ResvOverRun=0 
MinJobAge=3000
#OverTimeLimit=0 
SlurmctldTimeout=120
SlurmdTimeout=300
#UnkillableStepTimeout=60 
#VSizeFactor=0 
Waittime=0
# 
# 
# SCHEDULING 
#DefMemPerCPU=0 
FastSchedule=0
#MaxMemPerCPU=0 
#SchedulerRootFilter=1 
#SchedulerTimeSlice=30 
SchedulerType=sched/backfill
SchedulerPort=7321
SelectType=select/linear
SelectTypeParameters=CR_ONE_TASK_PER_CORE
# 
# 
# JOB PRIORITY 
#PriorityType=priority/basic 
#PriorityDecayHalfLife= 
#PriorityCalcPeriod= 
#PriorityFavorSmall= 
#PriorityMaxAge= 
#PriorityUsageResetPeriod= 
#PriorityWeightAge= 
#PriorityWeightFairshare= 
#PriorityWeightJobSize= 
#PriorityWeightPartition= 
#PriorityWeightQOS= 
# 
# 
# LOGGING AND ACCOUNTING 
#AccountingStorageEnforce=0 
AccountingStorageHost=%(master)s
AccountingStoragePass=%(dbpassword)s
AccountingStoragePort=3306
AccountingStorageType=accounting_storage/mysql
AccountingStorageUser=root
#AccountingStoreJobComment=YES
ClusterName=%(cluster-name)s
#DebugFlags= 
JobCompHost=%(master)s
#JobCompLoc=
JobCompPass=%(dbpassword)s
JobCompPort=3306
JobCompType=jobcomp/mysql
JobCompUser=root
JobAcctGatherFrequency=30
JobAcctGatherType=jobacct_gather/linux
SlurmctldDebug=4
SlurmctldLogFile=/var/log/slurmctld.log
SlurmdDebug=4
SlurmdLogFile=/var/log/slurmd.log
SlurmSchedLogFile=/var/log/slurmsched.log
SlurmSchedLogLevel=4
# 
# 
# POWER SAVE SUPPORT FOR IDLE NODES (optional) 
#SuspendProgram= 
#ResumeProgram= 
#SuspendTimeout= 
#ResumeTimeout= 
#ResumeRate= 
#SuspendExcNodes= 
#SuspendExcParts= 
#SuspendRate= 
#SuspendTime= 
# 
# 
# COMPUTE NODES 
NodeName=%(partitionlist)s  State=UNKNOWN
NodeName=%(fake-nodes)s State=FUTURE
PartitionName=compute Nodes=%(nodelist)s Default=YES MaxTime=INFINITE State=UP
"""

slurmdbd_conf_template = \
"""
AuthType=auth/munge
DbdHost=%(master)s
SlurmUser=root
StorageUser=root
StoragePass=%(dbpassword)s
StorageHost=master
StorageType=accounting_storage/mysql
DebugLevel=5
LogFile=/var/log/slurmdbd.log
ArchiveEvents=yes
ArchiveJobs=yes
ArchiveSteps=no
PurgeEventAfter=1month
PurgeJobAfter=12month
PurgeStepAfter=1month
LogFile=/var/log/slurmdbd.log"""
