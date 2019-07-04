.. index:: Missing Topologies

.. |element| replace:: :ref:`element <element>`
.. |elements| replace:: :ref:`elements <element>`
.. |topology| replace:: :ref:`topology <topology>`
.. |topologies| replace:: :ref:`topologies <topology>`
.. |decomposition| replace:: :doc:`decomposition <Decomposition>`
.. |theory predictions| replace:: :doc:`theory predictions <TheoryPredictions>`
.. |theory prediction| replace:: :doc:`theory prediction <TheoryPredictions>`
.. |constraint| replace:: :ref:`constraint <ULconstraint>`
.. |constraints| replace:: :ref:`constraints <ULconstraint>`
.. |intermediate states| replace:: :ref:`intermediate states <odd states>`
.. |final states| replace:: :ref:`final states <final states>`
.. |database| replace:: :ref:`database <Database>`
.. |bracket notation| replace:: :ref:`bracket notation <bracketNotation>`
.. |ExpRes| replace:: :ref:`Experimental Result<ExpResult>`
.. |ExpRess| replace:: :ref:`Experimental Results<ExpResult>`
.. |Database| replace:: :ref:`Database <Database>`
.. |Dataset| replace:: :ref:`DataSet<DataSet>`
.. |Datasets| replace:: :ref:`DataSets<DataSet>`
.. |results| replace:: :ref:`experimental results <ExpResult>`
.. |branches| replace:: :ref:`branches <branch>`
.. |branch| replace:: :ref:`branch <branch>`
.. |EMrs| replace:: :ref:`EM-type results <EMtype>`
.. |ULrs| replace:: :ref:`UL-type results <ULtype>`


.. _topCoverage:

Topology Coverage
=================


The constraints provided by SModelS are obviously limited
by its |database| and the available set of simplified model interpretations
provided by the experimental collaborations or computed by theory groups.
Therefore it is interesting to identify classes of missing simplified models
(or missing topologies) which are relevant for a given input model, but are
not constrained by the SModelS |database|. This task is performed
as a last step in SModelS, once the |decomposition| and the |theory predictions|
have been computed.

Given the |decomposition| output (list of |elements|), as well as the |database|
information, it finds and classifies the |elements| which are
not tested by any of the |results| in the |database|.
These elements are grouped into the following classes:

* *missingTopos*: |elements| which are not tested by any of the |results| in the |database| (independent of the element mass). The missing topologies are further classified as:

   * *displaced*: |elements| with at least one displaced decay;
   * *long-lived*: |elements| with at least one stable BSM particle other than the lightest one;
   * *prompt*: |elements| with MET final states only;

* *outsideGrid*: |elements| which could be tested by one or more experimental result, but are not constrained because the mass array is outside the mass grid;

In order to classify the |elements|, the tool loops over all the |elements| found in the
|decomposition| and checks if they are tested by one or more |results| in the |database| [*]_.
All the |elements| which are not tested by any of the |results| in the |database| (independent of their masses)
are added to the *missingTopos* class.
The remaining |elements| which do appear in one or more of the |results|, but have
not been tested because their masses fall outside the efficiency or upper limit grids (see |EMrs| and |ULrs|),
are added to the *outsideGrid* class.


Usually the list of  *missing* or *outsideGrid* elements is considerably long.
Hence, to compress this list, all |elements| differing only by their
masses (with the same |final states|) or electric charges are combined. Moreover, by default, electrons and muons
are combined to light leptons (denoted "l"), gluons and light quarks are combined into jets.


The topologies for each of the four categories are then grouped according to the final state.

Life time reweighting for missing topologies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _lifetimeWeightMissing:

Since the lifetime reweighting only takes place when an element is matched to an experimental result, the *missing* or *outsideGrid* elements
have not been reweighted accordingly.
The reweighting done on the database side is analysis dependent and can therefore not be applied to the unmatched elements.

SModelS computes the probability for prompt decay (:math:`\mathcal{F}_{prompt}`), for a displaced decay (:math:`\mathcal{F}_{displaced}`) 
as well as the probability for the particle to decay *outside* the detector (:math:`\mathcal{F}_{long}`). 
The branching fraction rescaled by :math:`\mathcal{F}_{long}` describes the probability of a decay where the daughter BSM state
traverses the detector (thus is considered stable),
while the branching fraction rescaled by :math:`\mathcal{F}_{prompt}` or :math:`\mathcal{F}_{displaced}` corresponds to a prompt or displaced
decay which will be followed by the next step in the cascade decay. This reweighting is illustrated in the figure below:

.. _decomp1b:

.. image:: images/decompScheme1.png
   :width: 90%
 
The precise values of :math:`\mathcal{F}_{prompt}`, :math:`\mathcal{F}_{displaced}` and :math:`\mathcal{F}_{long}` 
depend on the relevant detector size (:math:`L`), particle mass (:math:`M`), boost
(:math:`\beta`) and width (:math:`\Gamma`), thus
requiring a Monte Carlo simulation for each input model. Since these are analysis dependent quantities, we approximate 
the prompt,displaced and long-lived probabilities by:

.. math::
   \mathcal{F}_{long} = \exp(- \frac{\Gamma L_{outer}}{\langle \gamma \beta \rangle}) \mbox{ and } 
   \mathcal{F}_{prompt} = 1 - \exp(- \frac{\Gamma L_{inner}}{\langle \gamma \beta \rangle})
   \mathcal{F}_{displaced} = 1 - \mathcal{F}_{prompt} -\mathcal{F}_{long}
   
where :math:`L_{outer}` is the effective size of the detector (which we take to be 10 m for both ATLAS
and CMS), :math:`L_{inner}` is the effective radius of the inner detector (which we take to be 1 mm for both ATLAS
and CMS). Consequently, we call all decays taking place within :math:`L_{outer}` and outside of :math:`L_{inner}` displaced.

Finally, we take the effective time dilation factor to be  :math:`\langle \gamma \beta \rangle = 1.3` when
computing :math:`\mathcal{F}_{prompt}` and :math:`\langle \gamma \beta \rangle = 1.43` when computing :math:`\mathcal{F}_{long}`.
We point out that the above approximations are irrelevant if :math:`\Gamma` is very large (:math:`\mathcal{F}_{prompt} \simeq 1`
and :math:`\mathcal{F}_{long} \simeq 0`) or close to zero (:math:`\mathcal{F}_{prompt} \simeq 0`
and :math:`\mathcal{F}_{long} \simeq 1`). Only elements containing particles which have a considerable fraction of displaced
decays will be sensitive to the values chosen above.


The topology coverage tool is normally called from within SModelS (e.g. when running :ref:`runSModelS.py <runSModelS>`) by setting **testCoverage=True**
in the :ref:`parameters file <parameterFile>`.
In the output, contributions in each category are ordered by cross section. 
By default only the ones with the ten largest cross sections are shown.

* **The topology coverage tool is implemented by the** `Uncovered class <tools.html#tools.coverage.Uncovered>`_ 


.. [*] If :ref:`mass <massComp>` or :ref:`invisible compression <invComp>` are turned on, elements which can be :ref:`compressed <elementComp>` are not considered, to avoid double counting.
