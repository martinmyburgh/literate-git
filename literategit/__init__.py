import pygit2 as git
from collections import namedtuple


def _commit(repo, oid, required_n_parents=None, tag=None):
    commit = repo[oid]
    if not isinstance(commit, git.Commit):
        raise ValueError('not a Commit')
    parent_ids = commit.parent_ids
    n_parents = len(parent_ids)
    if required_n_parents is not None and n_parents != required_n_parents:
        raise ValueError('commit {} has {} parent/s so is not a {}'
                         .format(oid, n_parents, tag))
    return commit


class LeafCommit(namedtuple('LeafCommit', 'repo commit')):
    @classmethod
    def from_commit(cls, repo, oid):
        commit = _commit(repo, oid, 1, 'leaf-commit')
        return cls(repo, commit)


class SectionCommit(namedtuple('SectionCommit', 'repo commit children')):
    pass
